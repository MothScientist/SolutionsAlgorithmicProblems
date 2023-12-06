def sort_array(nums)
    if nums.length < 2
        nums
    elsif nums.length == 2
        nums[0], nums[1] = nums[1], nums[0] if nums[0] > nums[1]
        nums
    else
        left = nums[0, nums.length / 2]
        right = nums[nums.length / 2, nums.length - nums.length / 2]
        left = sort_array(left)
        right = sort_array(right)
        result = []
        li, ri = 0, 0
        while li < left.length && ri < right.length
            if left[li] < right[ri]
                result << left[li]
                li += 1
            elsif right[ri] < left[li]
                result << right[ri]
                ri += 1
            else
                result << left[li]
                result << right[ri]
                li += 1
                ri += 1
            end
        end
        result += left[li..-1] if li < left.length
        result += right[ri..-1] if ri < right.length
        result
    end
end